from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)
Faker.seed(42)

n_customers = 100
n_flights = 200

# Helper: random datetime
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# 1. Flights
flights = []
for i in range(n_flights):
    flight_id = f"DE{random.randint(1000, 9999)}"
    date = random_date(datetime(2025, 7, 1), datetime(2025, 8, 15))
    origin = random.choice(["FRA", "MUC", "BER", "DUS"])
    destination = random.choice(["PMI", "LIS", "ATH", "JFK", "CUN"])
    scheduled_time = date.strftime("%Y-%m-%d %H:%M")
    flights.append([flight_id, origin, destination, scheduled_time])

df_flights = pd.DataFrame(flights, columns=["flight_id", "origin", "destination", "scheduled_time"])

# 2. Notifications Sent
notifications = []
for i in range(n_customers):
    customer_id = i + 1
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    flight = random.choice(flights)
    flight_id = flight[0]
    notif_type = random.choice(["email", "sms"])
    notif_time = random_date(datetime(2025, 6, 25), datetime(2025, 8, 14))
    notifications.append([customer_id, name, email, phone, flight_id, notif_type, notif_time.strftime("%Y-%m-%d %H:%M")])

df_notifs = pd.DataFrame(notifications, columns=["customer_id", "name", "email", "phone", "flight_id", "notif_type", "notification_sent_at"])

# 3. Notification Events
notif_events = []
for row in df_notifs.itertuples():
    opened = random.choice([True, False])
    clicked = opened and random.choice([True, False])
    open_time = (datetime.strptime(row.notification_sent_at, "%Y-%m-%d %H:%M") + timedelta(hours=random.randint(1, 48))).strftime("%Y-%m-%d %H:%M") if opened else None
    click_time = (datetime.strptime(open_time, "%Y-%m-%d %H:%M") + timedelta(minutes=random.randint(5, 60))).strftime("%Y-%m-%d %H:%M") if clicked else None
    notif_events.append([row.customer_id, row.flight_id, opened, open_time, clicked, click_time])

df_events = pd.DataFrame(notif_events, columns=["customer_id", "flight_id", "opened", "opened_at", "clicked", "clicked_at"])

# 4. Customer Feedback
feedbacks = []
for row in df_notifs.sample(frac=0.3).itertuples():
    feedback_time = (datetime.strptime(row.notification_sent_at, "%Y-%m-%d %H:%M") + timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    issue = random.choice(["Didn't receive info", "Received late", "Confusing message", "No refund provided", "Customer service unresponsive"])
    feedbacks.append([row.customer_id, row.flight_id, issue, feedback_time])

df_feedback = pd.DataFrame(feedbacks, columns=["customer_id", "flight_id", "issue", "submitted_at"])

# 💾 Save to CSV
os.makedirs("../data", exist_ok=True)
df_flights.to_csv("../data/flights.csv", index=False)
df_notifs.to_csv("../data/notifications_sent.csv", index=False)
df_events.to_csv("../data/notification_events.csv", index=False)
df_feedback.to_csv("../data/customer_feedback.csv", index=False)

print("✅ Sample data generated in /data")
