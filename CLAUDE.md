This is a coursework project for Rosa's Pizza delivery-promise analysis.

## Commands

- Install dependencies: `python3 -m pip install -r requirements.txt`
- Run the app: `python3 -m streamlit run app.py`
- Open the local app at `http://localhost:8501`
- Stop the app with `Ctrl+C`

Use `python3 -m pip` and `python3 -m streamlit` rather than bare `pip`, `python`, or `streamlit`, because the active macOS environment does not reliably expose those commands on `PATH`.

## Architecture

- `Assignment_1.ipynb` is the source of truth for the Part II analysis logic.
- `rosa_logic.py` contains the notebook's two analysis functions: `calculate_late_cost` and `find_best_promise`.
- `rosa_logic.py` imports `delivery_times` from the `starter` package. It contains calculation logic only: no Streamlit UI, printing, or file I/O.
- `app.py` is the Streamlit interface. It imports `ZONES`, `TIME_BLOCKS`, and `COSTS` from `starter`, and imports the calculation functions from `rosa_logic.py`.
- `app.py` collects user inputs, calls the analysis functions when the user clicks the button, and displays the recommendation and expected net profit.
- Keep `app.py`, `rosa_logic.py`, and `requirements.txt` in the project root. Streamlit is launched with `app.py` as the main file.

## Notebook-to-app workflow

- The notebook is the source of truth. If the Part II formulas change, update the notebook first and then copy the tested functions unchanged into `rosa_logic.py`.
- Keep `seed=1` so the app produces the same reproducible results as the notebook.
- Do not rewrite or improve the analysis formulas while transferring them to the app.
- Validate app results against the notebook using the same zone, time block, promise range, costs, and seed.

## Constraints

- Preserve existing behavior unless asked to change it.
- Reuse the existing `starter` package and notebook logic rather than duplicating or hardcoding its data.
- Do not modify the `rosa-starter` package.
- Keep the costs dictionary keys consistent with `starter.COSTS`: `refund`, `churn_orders`, and `margin`.
- Validate that the minimum promise is smaller than the maximum and that the step is greater than zero before computing.
- Keep the default promise range at 30 to 90 minutes in steps of 5, matching the notebook.
- Do not add unrelated dependencies or restructure the project into a `src` layout unless explicitly requested.

## Expected result

With the default costs, promise range 30-90 in steps of 5, zone `Far West`, and time block `Fri/Sat eve`, the app should recommend a 55-minute promise with an expected net profit of $1,212.40, matching the notebook.
