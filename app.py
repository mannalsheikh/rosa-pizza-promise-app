import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS

from rosa_logic import calculate_late_cost, find_best_promise

st.set_page_config(page_title="Rosa's Pizza: Best Delivery Promise", page_icon="🍕")

st.title("🍕 Rosa's Pizza: Best Delivery Promise")
st.write(
    "Choose a zone and time block, set the range of promised delivery times to try, "
    "and adjust the costs. Then click the button to see the promise that earns the "
    "highest net profit."
)

# --- Sidebar: costs ---
st.sidebar.header("Costs")
margin = st.sidebar.number_input(
    "Profit margin per order ($)", min_value=0.0, value=float(COSTS["margin"]), step=0.5
)
churn_orders = st.sidebar.number_input(
    "Future orders lost per late order (churn)",
    min_value=0.0, value=float(COSTS["churn_orders"]), step=0.1,
)
refund = st.sidebar.number_input(
    "Refund per late order ($)", min_value=0.0, value=float(COSTS["refund"]), step=0.5
)
costs = {"refund": refund, "churn_orders": churn_orders, "margin": margin}
st.sidebar.metric("Total cost per late order", f"${calculate_late_cost(costs):,.2f}")

# --- Zone and time block ---
col1, col2 = st.columns(2)
zone = col1.selectbox("Zone", ZONES)
time_block = col2.selectbox("Time block", TIME_BLOCKS)

# --- Range of promises to try ---
st.subheader("Range of promised times to try (minutes)")
c1, c2, c3 = st.columns(3)
min_promise = c1.number_input("Minimum", min_value=1, value=30, step=5)
max_promise = c2.number_input("Maximum", min_value=1, value=90, step=5)
step = c3.number_input("Step", min_value=1, value=5, step=1)

if min_promise >= max_promise:
    st.error("The minimum must be smaller than the maximum.")
    st.stop()

promise_list = list(range(int(min_promise), int(max_promise) + 1, int(step)))
st.caption("Promises to try: " + ", ".join(str(p) for p in promise_list))

# --- Button: compute and save the result ---
if st.button("Find best promise", type="primary"):
    best_promise, net_profit = find_best_promise(zone, time_block, promise_list, costs)
    st.session_state["result"] = {
        "zone": zone,
        "time_block": time_block,
        "best_promise": best_promise,
        "net_profit": net_profit,
        "promise_list": promise_list,
        "costs": costs,
    }

# --- Show the result (stays on screen when inputs change) ---
result = st.session_state.get("result")
if result:
    st.subheader(f"Recommendation for {result['zone']} ({result['time_block']})")
    m1, m2 = st.columns(2)
    m1.metric("Recommended promise", f"{result['best_promise']} minutes")
    m2.metric("Expected net profit (4 weeks)", f"${result['net_profit']:,.2f}")

    tried = result["promise_list"]
    if result["best_promise"] in (tried[0], tried[-1]):
        st.warning(
            "The best promise is at the edge of the range you tried, so the true best "
            "may lie outside it. Try widening the range."
        )

    if (result["zone"], result["time_block"], result["promise_list"], result["costs"]) != (
        zone, time_block, promise_list, costs
    ):
        st.info("You changed an input since this result. Click the button to update it.")
