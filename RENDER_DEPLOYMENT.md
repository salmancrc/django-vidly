# 🚀 Deploy Vidly to Render (100% Free)

## 📋 What We Created

### **Files for Render Deployment:**

- ✅ `requirements.txt` - Python dependencies
- ✅ `build.sh` - Build script for Render
- ✅ `render.yaml` - Render configuration
- ✅ Updated `settings.py` - Production-ready

## 🎯 Step-by-Step Deployment

### **Step 1: Push to GitHub**

```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### **Step 2: Deploy on Render**

1. **Go to [render.com](https://render.com)**
2. **Sign up/Login** with GitHub
3. **Click "New +" → "Web Service"**
4. **Connect your GitHub repo**
5. **Select your vidly repository**
6. **Configure settings:**
   - **Name**: `vidly`
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn vidly.wsgi:application`
7. **Click "Create Web Service"**

### **Step 3: Add Database (Optional)**

1. **In Render dashboard, click "New +"**
2. **Select "PostgreSQL"**
3. **Name it**: `vidly-db`
4. **Click "Create Database"**
5. **Copy the "Internal Database URL"**

### **Step 4: Set Environment Variables**

In your web service settings, add:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=your-postgresql-url-from-step-3
ALLOWED_HOSTS=your-app-name.onrender.com
```

### **Step 5: Deploy**

- **Render auto-deploys** when you push to GitHub
- **First deployment** takes 5-10 minutes
- **Subsequent deployments** are faster

## 🎉 Your App is Live!

**URL**: `https://your-app-name.onrender.com`

## ⚡ Important Notes

### **Free Tier Limits:**

- **750 hours/month** (31 days)
- **Sleeps after 15 minutes** of inactivity
- **Cold start**: 15-30 seconds wake time
- **Perfect for**: Portfolio, demos, learning

### **What Each File Does:**

**`build.sh`** - Tells Render how to build your app:

- Install dependencies
- Collect static files
- Run migrations

**`render.yaml`** - Auto-configures everything:

- Web service settings
- Database setup
- Environment variables

**`settings.py`** - Production configuration:

- Environment-based settings
- PostgreSQL support
- Static file handling

## 🔧 Troubleshooting

### **Build Fails?**

- Check `requirements.txt` has all dependencies
- Verify `build.sh` is executable
- Check Render logs

### **Static Files Not Loading?**

- Whitenoise is configured in settings.py
- Static files collected during build

### **Database Issues?**

- Ensure DATABASE_URL is set
- Check PostgreSQL is created
- Run migrations manually if needed

### **500 Errors?**

- Set DEBUG=False in production
- Check Render logs
- Verify environment variables

## 🚀 Next Steps

1. **Custom Domain** (Optional)

   - In Render dashboard → Settings → Domains
   - Add your domain

2. **Monitor Usage**

   - Render dashboard shows usage
   - Free tier: 750 hours/month

3. **Scale Up** (When needed)
   - Upgrade to paid plan
   - No cold starts, better performance

## 📚 Support

- **Render Docs**: https://render.com/docs
- **Django Docs**: https://docs.djangoproject.com
- **Render Community**: https://community.render.com
