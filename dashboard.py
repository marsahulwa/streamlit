import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
bikesharing_df = pd.DataFrame({
    'Season_category': ['Spring', 'Summer', 'Fall', 'Winter'],
    'cntday': [2635.348185, 4995.253119, 5654.093194, 4765.366021]  # Sample values, you should replace it with your actual data
})

# Calculate average rental counts per season
avg_season = bikesharing_df.groupby('Season_category')['cntday'].mean().reset_index().sort_values("cntday")

# Streamlit app
st.title('Rata - Rata Penyewaan berdasarkan Musim')
st.write('Data Rata - Rata Penyewaan berdasarkan Musim:')
st.write(avg_season)

# Plot bar chart
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='cntday', y='Season_category', data=avg_season, palette='Set1', ax=ax)
ax.set_title('Rata - Rata Penyewaan berdasarkan Musim')
ax.set_xlabel('Rata - Rata Penyewaan')
ax.set_ylabel('Musim')

# Show plot in Streamlit
st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
bikesharing_df = pd.DataFrame({
    'weekday_category': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'cntday': [4239.505995, 4391.920936, 4566.708113, 4574.609293, 4703.503440, 4700.838359, 4561.544188]  # Sample values, you should replace it with your actual data
})

# Calculate average rental counts per weekday category
avg_weekday = bikesharing_df.groupby('weekday_category')['cntday'].mean().reset_index().sort_values("cntday")

# Streamlit app
st.title('Rata-rata Penyewaan Sepeda pada Hari Biasa')
st.write('Data Rata-rata Penyewaan Sepeda pada Hari Biasa:')
st.write(avg_weekday)

# Plot bar chart
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='weekday_category', y='cntday', data=avg_weekday, palette='Set1', ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda pada Hari Biasa')
ax.set_xlabel('Hari Biasa')
ax.set_ylabel('Rata-rata Penyewaan')

# Show plot in Streamlit
st.pyplot(fig)
