---
name: notebook-to-streamlit
description: Use when building or changing the Streamlit app (app.py) for Rosa's Pizza. Turns the analysis functions in Assignment_1.ipynb into a web app without rewriting their logic.
---

# notebook-to-streamlit

## Source of truth
- The logic lives in `Assignment_1.ipynb`, Part II: `calculate_late_cost(costs)` and
  `find_best_promise(zone, time_block, promise_list, costs, seed=1)`.
- The notebook uses `seed=1` so results are reproducible. Keep it in the app so the
  app's answers match the notebook.
- Copy these two functions unchanged into `rosa_logic.py`. That file must not import
  streamlit or print anything.
- `app.py` imports from `rosa_logic` and from `starter`. Do not rewrite or "improve"
  the formulas. If the logic needs to change, change the notebook first.
- Never hardcode zones, time blocks, costs or delivery times. Import `ZONES`,
  `TIME_BLOCKS`, `COSTS` and `delivery_times` from `starter`.

## What the app must let the user do
1. Pick a zone and a time block from dropdowns (`st.selectbox` over `ZONES` and `TIME_BLOCKS`).
2. Set the range of promised times to try: minimum, maximum and step, in minutes.
   Defaults match the notebook: 30, 90, 5.
3. Adjust the profit margin per order, churn per late order and refund per late order
   in the sidebar. Defaults come from `COSTS`.
4. Click a button to show the recommended promise and its expected net profit.

## Rules
- Validate the range before computing: minimum below maximum, step above 0.
  Otherwise show `st.error(...)` and call `st.stop()`.
- Build the promise list with `list(range(min, max + 1, step))` so the maximum is included.
- Build the costs dictionary with the same keys as `COSTS`: `refund`, `churn_orders`, `margin`.
- The button block only computes and saves the result to `st.session_state`. Show the
  result outside the button block so it stays on screen when another input changes.
  Label the result with the zone and time block it was computed for.
- If the recommended promise equals the smallest or largest promise tried, show a
  warning that the best promise may lie outside the range and suggest widening it.

## Deployment
`requirements.txt` lists `streamlit`, `numpy` and
`git+https://github.com/zhouy185/rosa-starter.git`.

## Done when
- `streamlit run app.py` starts with no errors.
- With default costs and the range 30–90 in steps of 5, Far West / Fri/Sat eve
  recommends 55 minutes with a net profit of $1,212.40, matching the notebook.
- After clicking the button, changing another input does not make the result disappear.
