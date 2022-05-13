import json
import os
import pandas as pd
import plotly
import plotly.graph_objects as go


input_cov_path = os.path.join(os.getcwd(), "data_sets", "pickledf", "covid.pickle")
input_influenza_path = os.path.join(os.getcwd(), "data_sets", "pickledf", "influenza.pickle")
cov_df = pd.read_pickle(input_cov_path)
flu_df = pd.read_pickle(input_influenza_path)


def cov_plot():
    print("show covid")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cov_df["Date_reported"], y=cov_df["New_cases"], name="infected", mode="lines+markers+text", text=cov_df["New_cases"], textposition="top left"))
    fig.add_trace(go.Scatter(x=cov_df["Date_reported"], y=cov_df["New_deaths"], name="deaths", mode="lines+markers+text", text=cov_df["New_deaths"], textposition="top left"))
    fig.update_layout(title="Covid-19 infections, and deaths 2020 in POLAND",
                        height=900,
                        xaxis=dict(
                            tickmode = 'array',
                            tickvals = cov_df["Date_reported"],
                            tickangle=300
                        ),
                        yaxis_title="People",
                        )
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def flu_plot():
    print("show flue")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=flu_df["Date"], y=flu_df["Confirmed"], name="infected", mode="lines+markers+text", text=flu_df["Confirmed"], textposition="top left"))
    fig.add_trace(go.Scatter(x=flu_df["Date"], y=flu_df["Deaths"], name="deaths", mode="lines+markers+text", text=flu_df["Deaths"], textposition="top left"))
    fig.update_layout(title="Influenza infections, and deaths 2020 in POLAND",
                        height=900,
                        xaxis=dict(
                            tickmode = 'array',
                            tickvals = flu_df["Date"],
                            tickangle=300
                        ),
                        yaxis_title="People",
                        )
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


if __name__ == '__main__':
    pass