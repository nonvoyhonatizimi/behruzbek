# PostgreSQL Migration Guide

This guide explains how to migrate from SQLite to PostgreSQL for the Behruzbek Tizimi.

## Prerequisites

1. PostgreSQL installed locally (for development)
2. Python 3.8+
3. pip

## Local Development Setup

### 1. Install PostgreSQL

**Windows:** Download from https://www.postgresql.org/download/windows/

**Mac:**
```bash
brew install postgresql
brew services start postgresql
```

**Linux:**
```bash
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
```

### 2. Create Database

```bash
# Login to PostgreSQL
sudo -u postgres psql

# Create database
CREATE DATABASE behruzbek;

# Create user (if needed)
CREATE USER your_username WITH PASSWORD 'your_password';

# Grant privileges
GRANT ALL PRIVILEGES ON DATABASE behruzbek TO your_username;

# Exit
\q
```

### 3. Setup Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your database credentials
DATABASE_URL=postgresql://username:password@localhost:5432/behruzbek
SECRET_KEY=your-secret-key-here
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Initialize Database

```bash
python init_db.py
```

### 6. Run the Application

```bash
python app.py
```

## Render Deployment

### 1. Set Environment Variables in Render Dashboard

Go to your Web Service → Environment → Add:

- **Key:** `DATABASE_URL`
- **Value:** `postgresql://postgres:YOUR_PASSWORD@db.YOUR_PROJECT.supabase.co:5432/postgres`

Replace `YOUR_PASSWORD` and `YOUR_PROJECT` with your actual Supabase credentials.

### 2. Deploy

Click "Manual Deploy" → "Deploy latest commit"

### 3. Initialize Database on Render

After deployment, go to Shell:

```bash
cd /opt/render/project/src
python init_db.py
```

## Database Migrations (Optional)

If you need to make schema changes in the future:

```bash
# Initialize migrations (one-time)
flask db init

# Create migration
flask db migrate -m "Description of changes"

# Apply migration
flask db upgrade
```

## Troubleshooting

### Connection Issues

1. Check if PostgreSQL is running:
   ```bash
   sudo service postgresql status
   ```

2. Verify DATABASE_URL format:
   ```
   postgresql://username:password@host:port/database
   ```

3. Check firewall settings for port 5432

### Migration Errors

If `flask db upgrade` fails:
```bash
# Reset migrations
rm -rf migrations/
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Data Persistence

With this setup:
- ✅ Data persists across deployments
- ✅ Data is stored in Supabase PostgreSQL
- ✅ Multiple users can access the same database
- ✅ Automatic backups (if configured in Supabase)
