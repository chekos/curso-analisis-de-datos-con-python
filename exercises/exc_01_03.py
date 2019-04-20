import altair as alt
from vega_datasets import data

source = data.us_employment()

alt.Chart(___).mark_bar().encode(
    x="___:T",
    y="nonfarm_change:Q",
    color=alt.condition(
        alt.datum.nonfarm_change > 0,
        alt.value("steelblue"),  # The positive color
        alt.value("____")  # The negative color
    )
).properties(width=___)
