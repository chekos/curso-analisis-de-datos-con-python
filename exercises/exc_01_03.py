# importa tus librerias
import ____ as alt
from vega_datasets import data

# tus datos
source = data.us_employment()

# crea una visualización
alt.Chart(____).mark_bar().encode(
    x="month:T",
    y="nonfarm_change:Q",
    color=alt.condition(
        alt.datum.nonfarm_change > 0,
        alt.value("steelblue"),  # The positive color
        alt.value("_____")  # The negative color
    )
).properties(width=600)
