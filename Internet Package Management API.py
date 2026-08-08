from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database
conn = sqlite3.connect("internet.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS packages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    package_name TEXT,
    price REAL
)
""")
conn.close()


# Add Package
@app.route("/packages", methods=["POST"])
def add_package():
    data = request.get_json()

    conn = sqlite3.connect("internet.db")

    conn.execute(
        """
        INSERT INTO packages(customer_name, package_name, price)
        VALUES (?, ?, ?)
        """,
        (
            data["customer_name"],
            data["package_name"],
            data["price"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Package Added Successfully"}), 201


# Get All Packages
@app.route("/packages", methods=["GET"])
def get_packages():

    conn = sqlite3.connect("internet.db")
    conn.row_factory = sqlite3.Row

    packages = conn.execute(
        "SELECT * FROM packages"
    ).fetchall()

    conn.close()

    return jsonify([dict(package) for package in packages])


# Update Package
@app.route("/packages/<int:id>", methods=["PUT"])
def update_package(id):

    data = request.get_json()

    conn = sqlite3.connect("internet.db")

    conn.execute(
        """
        UPDATE packages
        SET customer_name=?, package_name=?, price=?
        WHERE id=?
        """,
        (
            data["customer_name"],
            data["package_name"],
            data["price"],
            id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Package Updated Successfully"})


# Delete Package
@app.route("/packages/<int:id>", methods=["DELETE"])
def delete_package(id):

    conn = sqlite3.connect("internet.db")

    conn.execute(
        "DELETE FROM packages WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Package Deleted Successfully"})


if __name__ == "__main__":
    app.run(debug=True)