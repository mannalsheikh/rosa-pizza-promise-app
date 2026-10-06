---
name: notebook-to-streamlit
description: Turns the Part II analysis functions in Assignment_1.ipynb into a Streamlit web app that helps Rosa's Pizza choose the most profitable delivery promise. Use when building, changing or deploying the Streamlit app (app.py) for this project.
---

# notebook-to-streamlit

## Purpose and scope

This skill converts the tested logic in `Assignment_1.ipynb` into a Streamlit app
without rewriting it, so the app and the notebook always give the same answer.

**In scope:** building or changing `app.py`, `rosa_logic.py` and `requirements.txt`,
and preparing the app for Streamlit Community Cloud.

**Out of scope:** changing the analysis itself (Parts I and II of the notebook), and
editing the `rosa-starter` package.

## Workflow

1. **Read the notebook.** Find `calculate_late_cost(costs)` and
   `find_best_promise(zone, time_block, promise_list, costs, seed=1)` in Part II.
2. **Copy the logic.** Paste both functions unchanged into `rosa_logic.py`, importing
   `delivery_times` from `starter`.
3. **Build the app in `app.py`.** It must let the user:
   1. pick a zone and a time block from dropdowns (`st.selectbox` over `ZONES` and
      `TIME_BLOCKS`);
   2. set the range of promised times to try: minimum, maximum and step, in minutes
      (defaults 30, 90 and 5, matching the notebook);
   3. adjust the profit margin per order, churn per late order and refund per late
      order in the sidebar (defaults from `COSTS`);
   4. click a button to see the recommended promise and its expected net profit.
4. **Write `requirements.txt`** with `streamlit`, `numpy` and
   `git+https://github.com/zhouy185/rosa-starter.git`.
5. **Test locally** with `streamlit run app.py` and check the results against the
   notebook (see "Done when").
6. **Deploy** by pushing to GitHub and creating the app on Streamlit Community Cloud
   with main file `app.py`.

## Requirements and constraints

### Expected files
| File | Contents |
|---|---|
| `rosa_logic.py` | The two notebook functions only. No `streamlit` import, no `print`. |
| `app.py` | The Streamlit interface. Imports from `rosa_logic` and `starter`. |
| `requirements.txt` | `streamlit`, `numpy` and the `rosa-starter` git line. |

### Rules
- **The notebook is the source of truth.** Do not rewrite or "improve" the formulas.
  If the logic needs to change, change the notebook first, then copy it again.
- **Never hardcode data.** Import `ZONES`, `TIME_BLOCKS`, `COSTS` and
  `delivery_times` from `starter`.
- **Keep `seed=1`** so the app's results match the notebook exactly.
- **Validate the range before computing:** minimum below maximum, step above 0.
  Otherwise show `st.error(...)` and call `st.stop()`.
- Build the promise list with `list(range(min, max + 1, step))` so the maximum is included.
- Build the costs dictionary with the same keys as `COSTS`: `refund`, `churn_orders`, `margin`.
- The button only computes and saves the result to `st.session_state`. Show the result
  outside the button block so it stays on screen when another input changes, and label
  it with the zone and time block it was computed for.
- If the recommended promise equals the smallest or largest promise tried, show a
  warning that the best promise may lie outside the range and suggest widening it.

### Limitations
- Results come from a simulator. They are reproducible only because of `seed=1`.
- The app recommends one zone and time block at a time.
- Driver staffing is fixed and not part of the model.

## Done when
- `streamlit run app.py` starts with no errors.
- With default costs and the range 30–90 in steps of 5, Far West / Fri/Sat eve
  recommends **55 minutes** with a net profit of **$1,212.40**, matching the notebook.
- After clicking the button, changing another input does not make the result disappear.

## Additional notes
- Streamlit Community Cloud installs packages from `requirements.txt`, so `app.py`,
  `rosa_logic.py` and `requirements.txt` must stay in the repository root.
- Free Streamlit apps sleep after a few days without visits; opening the link wakes them.
- The repository is public, so do not add personal information to any file.
