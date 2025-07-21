from flask import Flask, request, jsonify
from supabase import create_client, Client
from postgrest.exceptions import APIError

app = Flask(__name__)

url: str = "https://lgztvgybalhvppkfpwdc.supabase.co"
key: str = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxnenR2Z3liYWxodnBwa2Zwd2RjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQzNDkwMTQsImV4cCI6MjA1OTkyNTAxNH0.JfB6J38LmdlvUwIgkdRmQcBDnv6OzFaA-D27S0ylVnA"
)
supabase: Client = create_client(url, key)


@app.route("/")
def route_root():
    return ""


@app.get("/mail")
def get_mail():
    response = supabase.table("mail").select("*").execute()
    return response.data


@app.get("/inventory")
def get_inventory():
    response = supabase.table("inventory").select("*").execute()
    return response.data


@app.post("/inventory")
def post_inventory():
    request_data = request.get_json()
    
    try:
        response = supabase.table("inventory").insert(request_data).execute()
        return jsonify(response.data), 201

    except APIError as e:

        return jsonify({
            "error": e.message,
            "code": e.code,
            "details": e.details
        }), 400


@app.get("/subscription")
def get_subscription():
    response = supabase.table("subscription").select("*").execute()
    return response.data
