import urllib.request as ur
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

airQualityHR = ur.urlopen(url).read()
root = ET.fromstring(airQualityHR)


df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))


i = 0
while True:
    try:
        obj = root[i]
    except:
        break

    row = {
        'mjerenje': float(obj[0].text),
        'vrijeme': obj[2].text
    }

    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    i = i + 1

df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)


print("Prvih 5 mjerenja:")
print(df.head())

df.plot(x='vrijeme', y='mjerenje', title="PM10 Osijek 2017")
plt.show()


top3 = df.sort_values(by='mjerenje', ascending=False).head(3)

print("\nTri datuma s najvećom koncentracijom PM10:")
print(top3[['vrijeme', 'mjerenje']])


df['month'] = df['vrijeme'].dt.month
df['dayOfweek'] = df['vrijeme'].dt.dayofweek