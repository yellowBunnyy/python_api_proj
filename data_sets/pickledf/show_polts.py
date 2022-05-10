import pandas as pd
import os
import plotly.graph_objects as go

print("show PLOTS ||||")


input_cov_path = os.path.join(os.getcwd(), "src", "pickledf", "covid.pickle")
input_influenza_path = os.path.join(os.getcwd(), "src", "pickledf", "influenza.pickle")
cov_df = pd.read_pickle(input_cov_path)
flu_df = pd.read_pickle(input_influenza_path)


def cov_plot():
    print("show covid")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cov_df["Date_reported"], y=cov_df["New_cases"], name="infected"))
    fig.add_trace(go.Scatter(x=cov_df["Date_reported"], y=cov_df["New_deaths"], name="deaths"))
    fig.update_layout(title="Covid-19 infections, and deaths 2020 in POLAND",
                        xaxis=dict(
                            tickmode = 'array',
                            tickvals = cov_df["Date_reported"],
                            tickangle=300
                        ),
                        yaxis_title="People",
                        )
    fig.show()


def flu_plot():
    print("show flue")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=flu_df["Date"], y=flu_df["Confirmed"], name="infected"))
    fig.add_trace(go.Scatter(x=flu_df["Date"], y=flu_df["Deaths"], name="deaths"))
    fig.update_layout(title="Influenza infections, and deaths 2020 in POLAND",
                        xaxis=dict(
                            tickmode = 'array',
                            tickvals = flu_df["Date"],
                            tickangle=300
                        ),
                        yaxis_title="People",
                        )
    fig.show()


if __name__ == '__main__':
    cov_plot()
    flu_plot()
