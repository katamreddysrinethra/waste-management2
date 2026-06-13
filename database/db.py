import sqlite3
from pathlib import Path

DB_NAME = "ecocycle.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()

    schema_path = Path("database/schema.sql")

    with open(schema_path, "r") as file:
        conn.executescript(file.read())

    conn.commit()
    conn.close()


def execute_query(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()

    result = cursor.fetchall()

    conn.close()

    return result


def insert_query(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()

    last_id = cursor.lastrowid

    conn.close()

    return last_id


def create_pickup_request(
    user_id,
    waste_type,
    quantity,
    address,
    pickup_date,
    image_path,
    notes
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO pickup_requests
        (
            user_id,
            waste_type,
            quantity,
            address,
            pickup_date,
            image_path,
            notes
        )
        VALUES
        (?,?,?,?,?,?,?)
        """,
        (
            user_id,
            waste_type,
            quantity,
            address,
            pickup_date,
            image_path,
            notes
        )
    )

    conn.commit()
    conn.close()


def get_user_pickups(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM pickup_requests
        WHERE user_id=?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_all_pickups():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM pickup_requests
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
def get_pending_pickups():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM pickup_requests
        WHERE status='Pending'
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def assign_pickup(
    pickup_id,
    collector_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE pickup_requests
        SET status='In Progress'
        WHERE id=?
    """,(pickup_id,))

    cursor.execute("""
        INSERT INTO pickup_assignments
        (pickup_id, collector_id)
        VALUES (?,?)
    """,(pickup_id,collector_id))

    conn.commit()

    conn.close()


def get_collector_pickups(
    collector_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.*
        FROM pickup_requests p
        JOIN pickup_assignments pa
        ON p.id = pa.pickup_id
        WHERE pa.collector_id=?
    """,(collector_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def update_pickup_status(
    pickup_id,
    status
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE pickup_requests
        SET status=?
        WHERE id=?
    """,(status,pickup_id))

    conn.commit()

    conn.close()


def update_user_points(
    user_id,
    points,
    reason
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET points = points + ?
        WHERE id=?
    """,(points,user_id))

    cursor.execute("""
        INSERT INTO rewards
        (
            user_id,
            points,
            reason
        )
        VALUES
        (?,?,?)
    """,
    (
        user_id,
        points,
        reason
    ))

    conn.commit()

    conn.close()


def get_leaderboard():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        full_name,
        points
        FROM users
        ORDER BY points DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def log_activity(
    user_id,
    action
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO activity_logs
        (
            user_id,
            action
        )
        VALUES
        (?,?)
    """,
    (
        user_id,
        action
    ))

    conn.commit()

    conn.close()
# --------------------
# COMPLAINTS
# --------------------

def create_complaint(
    user_id,
    complaint_type,
    title,
    description,
    image_path
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO complaints
        (
            user_id,
            complaint_type,
            title,
            description,
            image_path
        )
        VALUES
        (?,?,?,?,?)
    """,
    (
        user_id,
        complaint_type,
        title,
        description,
        image_path
    ))

    conn.commit()

    conn.close()


def get_user_complaints(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM complaints
        WHERE user_id=?
        ORDER BY created_at DESC
    """,(user_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_all_complaints():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM complaints
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def update_complaint_status(
    complaint_id,
    status
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status=?
        WHERE id=?
    """,
    (
        status,
        complaint_id
    ))

    conn.commit()

    conn.close()    
# --------------------
# MARKETPLACE
# --------------------

def create_marketplace_listing(
    material_type,
    quantity,
    price,
    description,
    seller_id
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO marketplace
        (
            material_type,
            quantity,
            price,
            description,
            seller_id
        )
        VALUES (?,?,?,?,?)
    """,
    (
        material_type,
        quantity,
        price,
        description,
        seller_id
    ))

    conn.commit()
    conn.close()


def get_marketplace_items():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM marketplace
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def create_transaction(
    marketplace_id,
    buyer_id,
    quantity,
    total_amount
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (
            marketplace_id,
            buyer_id,
            quantity,
            total_amount
        )
        VALUES
        (?,?,?,?)
    """,
    (
        marketplace_id,
        buyer_id,
        quantity,
        total_amount
    ))

    conn.commit()

    conn.close()    