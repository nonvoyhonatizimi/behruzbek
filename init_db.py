#!/usr/bin/env python3
"""
Database initialization script for Behruzbek Tizimi
Run this after setting up your PostgreSQL database
"""

import os
from app import app, db
from models import User, Customer

def init_database():
    """Initialize database with tables and default data"""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✅ Tables created successfully!")
        
        # Create default admin if not exists
        if not User.query.filter_by(login='rovshanbek').first():
            admin = User(login='rovshanbek', parol='admin0257', rol='admin', ism='Rovshanbek')
            db.session.add(admin)
            db.session.commit()
            print("✅ Default admin user created")
        
        # Add default customers if not exist
        customers_to_add = [
            "behruzbek", "doston", "sanjar patir", "noilaxon", "ziyo patir",
            "turonboy", "shirin patir", "xojamboy", "azizbek patir", "akmal patir",
            "shukurullo patir", "abduqahor patir", "milyon patir", "ramshit patir",
            "xusanboy patir", "ishonch patir", "soxib patir", "sardor patir",
            "lazzat patir", "paxlavon patir", "tanxo patir", "alisher patir",
            "asil patir", "sarvar patir", "javohir patir", "kozim patir",
            "klara opa", "rashid patir", "nodir patir", "rokiya patir",
            "xayotjon", "shaxboz patir", "osiyo patir", "ozbegim",
            "sadiya patir", "ifor patir", "diyor patir", "lazzat patir2",
            "mamura qirchin", "dilafruz qirchin", "saroy patir", "abbosxon qirchin",
            "nasiba qirchin", "abdulatif", "pungan baliq", "tomchi dangara", "benazir"
        ]
        
        added_count = 0
        for customer_name in customers_to_add:
            if not Customer.query.filter_by(nomi=customer_name).first():
                new_customer = Customer(
                    nomi=customer_name,
                    turi='dokon',
                    telefon='',
                    manzil='',
                    kredit_limit=0,
                    jami_qarz=0
                )
                db.session.add(new_customer)
                added_count += 1
        
        db.session.commit()
        print(f"✅ {added_count} customers added to database")
        print("\n🎉 Database initialization complete!")

if __name__ == '__main__':
    init_database()
