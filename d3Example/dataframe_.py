import pandas as pd
import json

df = pd.read_csv('d3Example/data/data.csv').drop('Open', axis=1)

df2 = df[['Date', 'Close']]
df2
print(df)
# chart_data = df.to_dict(orient='records')
# chart_data = json.dumps(chart_data, indent=2)
# data = {'chart_data': chart_data}
    # return render_template("index.html", data=data)
