A2B HOSPITAL WEBSITE - CLEAN DEPLOYMENT NOTES

Changes in this copy:
- Kept the Django project, existing templates, migrations, requirements and static assets.
- Added static fallback cards to the homepage so department and doctor images still appear when the hosted database has no rows.
- Removed generated staticfiles, Python cache files, Git history, local SQLite database, and unrelated temporary log files from this ZIP.

IMPORTANT FOR VERCEL
1. Vercel > Project > Settings > Environment Variables.
2. Confirm DATABASE_URL is the Neon PostgreSQL connection string and is enabled for Production (not only Preview/Development).
3. Redeploy after changing environment variables.
4. Django migrations must be applied to that same Neon database. Run locally from this project folder in PowerShell after setting the real connection string:
   $env:DATABASE_URL = "YOUR_NEON_POSTGRES_CONNECTION_STRING"
   python manage.py migrate
   Do not paste the connection string publicly.
5. The local SQLite database is intentionally not included in this cleaned ZIP. Users/passwords from local SQLite do not automatically transfer to Neon. Use the site's Register page to create a new account after migrations succeed.

Vercel runtime logs previously showed sqlite3.OperationalError: unable to open database file. That means the deployed runtime was using SQLite instead of DATABASE_URL. If this continues, verify DATABASE_URL's Production scope and redeploy. The build log saying "Build Completed" does not confirm that the runtime database is connected.
