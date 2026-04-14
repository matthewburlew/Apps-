import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(
    page_title="Memorabilia Vault",
    page_icon="⚾",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0a;
    color: #f0ece0;
}

.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #111418 100%);
}

h1, h2, h3 {
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 2px;
}

.vault-header {
    background: linear-gradient(90deg, #b8860b, #ffd700, #b8860b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 4rem;
    letter-spacing: 4px;
    line-height: 1;
    margin-bottom: 0;
}

.subtitle {
    color: #888;
    font-size: 0.95rem;
    font-weight: 300;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 0;
    margin-bottom: 2rem;
}

.metric-card {
    background: #161616;
    border: 1px solid #2a2a2a;
    border-left: 3px solid #ffd700;
    border-radius: 4px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
}

.metric-label {
    font-size: 0.7rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 0.3rem;
}

.metric-value {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    color: #ffd700;
    letter-spacing: 1px;
}

.stButton > button {
    background: linear-gradient(90deg, #b8860b, #ffd700);
    color: #0a0a0a;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.1rem;
    letter-spacing: 2px;
    border: none;
    border-radius: 2px;
    padding: 0.6rem 2rem;
    width: 100%;
    cursor: pointer;
    transition: opacity 0.2s;
}

.stButton > button:hover {
    opacity: 0.85;
}

.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div,
.stRadio > div {
    background-color: #161616 !important;
    border-color: #2a2a2a !important;
    color: #f0ece0 !important;
}

div[data-testid="stSidebar"] {
    background-color: #0f0f0f;
    border-right: 1px solid #1e1e1e;
}

.stDataFrame {
    border: 1px solid #2a2a2a;
    border-radius: 4px;
}

.divider {
    border: none;
    border-top: 1px solid #1e1e1e;
    margin: 2rem 0;
}

.section-label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.6rem;
    letter-spacing: 3px;
    color: #f0ece0;
    margin-bottom: 1rem;
}

.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: #444;
    border: 1px dashed #2a2a2a;
    border-radius: 4px;
}

.empty-state .icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.empty-state p {
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.delete-btn > button {
    background: linear-gradient(90deg, #8b0000, #cd5c5c) !important;
    color: #fff !important;
    font-size: 0.85rem !important;
    padding: 0.3rem 1rem !important;
    letter-spacing: 1px !important;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="vault-header">⚾ Memorabilia Vault</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Baseball Collection Tracker & Valuation Tool</p>', unsafe_allow_html=True)

# --- Base Value Logic ---
base_values = {
    "Signed Baseball": 150,
    "Signed Jersey": 400,
    "Rookie Card": 300,
    "Photo": 75,
    "Bat": 350,
    "Helmet": 500,
    "Bobblehead": 40
}

condition_multipliers = {
    "Poor": 0.3,
    "Fair": 0.6,
    "Good": 1.0,
    "Excellent": 1.5,
    "Mint": 2.0
}

# --- Session State ---
if "collection" not in st.session_state:
    st.session_state.collection = []

# --- Sidebar ---
with st.sidebar:
    st.markdown('<p style="font-family: Bebas Neue; font-size:1.4rem; letter-spacing:3px; color:#ffd700;">ADD ITEM</p>', unsafe_allow_html=True)

    player_name = st.text_input("Player Name", placeholder="e.g. Shohei Ohtani")
    item_type = st.selectbox("Item Type", list(base_values.keys()))
    condition = st.radio("Condition", list(condition_multipliers.keys()), index=2)
    year = st.number_input("Year", min_value=1900, max_value=2025, value=2020)
    notes = st.text_area("Notes (optional)", placeholder="e.g. Authenticated by PSA, bought at auction...")

    if player_name.strip():
        est = round(base_values[item_type] * condition_multipliers[condition], 2)
        st.markdown(f"""
        <div class="metric-card" style="margin-top:1rem;">
            <div class="metric-label">Estimated Value</div>
            <div class="metric-value">${est:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    add_item = st.button("ADD TO VAULT")

    if add_item:
        if player_name.strip() == "":
            st.warning("Enter a player name first.")
        else:
            est = round(base_values[item_type] * condition_multipliers[condition], 2)
            st.session_state.collection.append({
                "Player": player_name.strip(),
                "Item Type": item_type,
                "Condition": condition,
                "Year": int(year),
                "Est. Value ($)": est,
                "Notes": notes.strip() if notes.strip() else "—"
            })
            st.success(f"Added to vault!")

# --- Main Content ---
if st.session_state.collection:
    df = pd.DataFrame(st.session_state.collection)

    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Items</div>
            <div class="metric-value">{len(df)}</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Est. Value</div>
            <div class="metric-value">${df['Est. Value ($)'].sum():,.0f}</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Avg Item Value</div>
            <div class="metric-value">${df['Est. Value ($)'].mean():,.0f}</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        top_item = df.loc[df['Est. Value ($)'].idxmax(), 'Player']
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Top Valued Item</div>
            <div class="metric-value" style="font-size:1.2rem;">{top_item}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # --- Filter + Sort Controls ---
    st.markdown('<p class="section-label">Collection</p>', unsafe_allow_html=True)

    ctrl1, ctrl2, ctrl3 = st.columns([2, 1.5, 1.5])
    with ctrl1:
        search = st.text_input("", placeholder="🔍 Filter by player...")
    with ctrl2:
        sort_by = st.selectbox("Sort By", ["Est. Value ($)", "Year", "Condition", "Player", "Item Type"])
    with ctrl3:
        sort_order = st.radio("Order", ["Descending", "Ascending"], horizontal=True)

    # Apply filter
    filtered_df = df.copy()
    if search:
        filtered_df = filtered_df[filtered_df["Player"].str.contains(search, case=False)]

    # Apply sort
    ascending = sort_order == "Ascending"
    filtered_df = filtered_df.sort_values(by=sort_by, ascending=ascending).reset_index(drop=True)

    # Display table
    st.dataframe(
        filtered_df.style.format({"Est. Value ($)": "${:,.2f}"}),
        use_container_width=True,
        hide_index=True
    )

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # --- Delete Item ---
    st.markdown('<p class="section-label">Remove Item</p>', unsafe_allow_html=True)

    del_col1, del_col2 = st.columns([3, 1])
    with del_col1:
        item_labels = [
            f"{i+1}. {row['Player']} — {row['Item Type']} ({row['Condition']}, {row['Year']}) — ${row['Est. Value ($)']:,.0f}"
            for i, row in df.iterrows()
        ]
        item_to_delete = st.selectbox("Select item to remove", item_labels)
    with del_col2:
        st.markdown('<div style="margin-top:1.75rem;"></div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="delete-btn">', unsafe_allow_html=True)
            if st.button("REMOVE FROM VAULT"):
                idx = item_labels.index(item_to_delete)
                st.session_state.collection.pop(idx)
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # --- Export CSV ---
    st.markdown('<p class="section-label">Export Collection</p>', unsafe_allow_html=True)

    export_col1, export_col2 = st.columns([3, 1])
    with export_col1:
        st.markdown('<p style="color:#888; font-size:0.85rem; letter-spacing:1px;">Download your full collection as a CSV file for record keeping or further analysis.</p>', unsafe_allow_html=True)
    with export_col2:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="EXPORT AS CSV",
            data=csv,
            file_name="memorabilia_vault.csv",
            mime="text/csv"
        )

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # --- Chart ---
    st.markdown('<p class="section-label">Value by Item Type</p>', unsafe_allow_html=True)
    chart_data = df.groupby("Item Type")["Est. Value ($)"].sum().reset_index()
    st.bar_chart(chart_data.set_index("Item Type"), color="#ffd700")

else:
    st.markdown("""
    <div class="empty-state">
        <div class="icon">⚾</div>
        <p>Your vault is empty — add items using the sidebar</p>
    </div>
    """, unsafe_allow_html=True)