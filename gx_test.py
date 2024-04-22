import pandas as pd
from datetime import timedelta

def find_time_gaps(df, column_name, granularity='days'):
    
    valid_granularities = ['days', 'hours', 'minutes', 'seconds']
    if granularity not in valid_granularities:
        raise ValueError("Granularidade inválida. Escolha entre 'days', 'hours', 'minutes' ou 'seconds'.")
    
    if not pd.api.types.is_datetime64_any_dtype(df[column_name]):
        raise TypeError("A coluna especificada não é do tipo datetime.")

    df.sort_values(by=column_name, inplace=True)

    min_date = df[column_name].min()
    max_date = df[column_name].max()

    if granularity == 'days':
        all_dates = [min_date + timedelta(days=i) for i in range((max_date - min_date).days)]
    elif granularity == 'hours':
        all_dates = [min_date + timedelta(hours=i) for i in range(int((max_date - min_date).total_seconds() / 3600) + 1)]
    elif granularity == 'minutes':
        all_dates = [min_date + timedelta(minutes=i) for i in range(int((max_date - min_date).total_seconds() / 60) + 1)]
    else:
        all_dates = [min_date + timedelta(seconds=i) for i in range(int((max_date - min_date).total_seconds()) + 1)]

    
    for date in df[column_name]:
        if date in all_dates:
            all_dates.remove(date)

    return all_dates



if __name__ == "__main__":
    
    data = {
        'timestamp': [
            '2024-04-01 12:00:00',
            '2024-04-01 12:05:00',
            '2024-04-01 12:15:00',
            '2024-04-01 12:30:00',
            '2024-04-01 12:35:00',
            '2024-04-01 12:55:00',
            '2024-04-01 14:00:00',
            '2024-04-01 14:10:00',
            '2024-04-01 14:20:00',
        ]
    }

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    missing_dates = find_time_gaps(df, 'timestamp', granularity='hours')
    print("Valores faltantes:", missing_dates)
