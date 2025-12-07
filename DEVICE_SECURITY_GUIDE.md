# Device Security Quick Start Guide

## Securing Your Account When Switching to an Apple Device

This guide helps you quickly secure your account by logging out all other devices when you switch to using an Apple device.

## Why Log Out Other Devices?

When switching to a new Apple device, it's a security best practice to end all active sessions on other devices. This ensures:

- Only your new Apple device has access to your account
- No unauthorized devices remain logged in
- Your data is protected if previous devices were lost or compromised
- Better control over which devices can access your account

## Quick Steps to Log Out All Other Devices

### Method 1: During Apple Device Setup

1. Open the application on your new Apple device
2. Log in with your credentials
3. When prompted "Log out other devices?", select **Yes**
4. Authenticate with Face ID, Touch ID, or your device passcode
5. All other devices will be immediately logged out

### Method 2: From Security Settings

1. Log in to your account on your Apple device
2. Tap your profile icon in the top right
3. Navigate to **Settings** → **Security & Privacy**
4. Tap **Active Sessions** or **Manage Devices**
5. Tap **Log Out All Other Devices**
6. Confirm with your password or biometric authentication

### Method 3: Emergency Logout

If you suspect unauthorized access:

1. Open any browser or the app
2. Go to the login page
3. Tap **Forgot Password?**
4. Follow the password reset process
5. Check the option **"Log out all devices after reset"**
6. Your password will be reset and all devices will be logged out

## What Happens When You Log Out Other Devices?

- **Immediate Effect**: All other active sessions are terminated within seconds
- **Device Notification**: Other devices will show a "Session expired" message
- **Data Safety**: No data is deleted from other devices, only the session is ended
- **Re-login Required**: You'll need to log in again on those devices if you want to use them

## After Logging Out Other Devices

### On Your Apple Device

Your current session remains active. You can:

- ✅ Continue using the application normally
- ✅ Access all your emails and social media accounts
- ✅ Manage your settings and preferences
- ✅ Set up automatic backup to iCloud

### On Other Devices

Other devices will:

- ❌ Be logged out immediately
- ❌ Lose access to your account
- ❌ Show a "Session ended" or "Please log in again" message
- ℹ️ Can log back in anytime with your credentials

## Setting Up Your Apple Device for Enhanced Security

### 1. Enable Biometric Authentication

**For iPhone/iPad with Face ID:**
```
Settings → Face ID & Passcode → Turn On Face ID
→ Select "Use Face ID for Expert Pancake"
```

**For Devices with Touch ID:**
```
Settings → Touch ID & Passcode → Turn On Touch ID
→ Select "Use Touch ID for Expert Pancake"
```

### 2. Enable Two-Factor Authentication

1. Go to **Settings** → **Security & Privacy**
2. Tap **Two-Factor Authentication**
3. Choose verification method:
   - SMS to your phone number
   - Authentication app (recommended)
   - Email verification
4. Complete setup by entering the verification code

### 3. Set Up Automatic Logout

For additional security, enable automatic logout on inactivity:

1. **Settings** → **Security & Privacy** → **Auto-Logout**
2. Choose timeout period:
   - 15 minutes (High security)
   - 1 hour (Balanced)
   - 4 hours (Convenience)
   - Never (Not recommended)

### 4. Enable Login Notifications

Get notified when someone logs into your account:

1. **Settings** → **Notifications** → **Security Alerts**
2. Enable **New Device Login**
3. Choose notification method:
   - Push notification to this device
   - Email alert
   - SMS alert (optional)

## Monitoring Active Sessions

### Regular Session Review

Check your active sessions weekly:

1. **Settings** → **Security & Privacy** → **Active Sessions**
2. Review the list of active devices
3. Look for:
   - Unfamiliar device names
   - Unusual locations
   - Old devices you no longer use
4. Remove any suspicious or unused sessions

### Understanding Session Information

Each session shows:

- **Device Name**: e.g., "John's iPhone 13"
- **Device Type**: iPhone, iPad, Mac, Windows PC, Android, etc.
- **Operating System**: iOS 17.1, macOS Sonoma, etc.
- **Browser/App**: Safari, Chrome, or mobile app
- **IP Address**: Your internet connection's IP
- **Location**: Approximate city based on IP
- **Last Active**: When the device last accessed your account
- **Current Session**: Highlighted if it's your current device

### Session Security Status

- 🟢 **Trusted Device**: Verified and frequently used
- 🟡 **New Device**: Recently added, pending verification
- 🔴 **Suspicious**: Unfamiliar location or device

## Troubleshooting

### Problem: I logged out all devices but someone is still accessing my account

**Solution:**
1. Change your password immediately
2. Enable two-factor authentication
3. Review and revoke third-party app access
4. Check for any email forwarding rules
5. Contact support if the issue persists

### Problem: I can't log out other devices

**Solution:**
1. Ensure you're logged in with the account owner credentials
2. Check your internet connection
3. Update the app to the latest version
4. Try logging out from the web interface instead
5. Contact support if the problem continues

### Problem: My device keeps getting logged out

**Solution:**
1. Check if someone else has access to your account
2. Verify your device is marked as "Trusted"
3. Ensure your iOS/macOS is up to date
4. Check your auto-logout settings
5. Disable and re-enable biometric authentication

## Best Practices Summary

✅ **DO:**
- Log out other devices when switching to your Apple device
- Enable two-factor authentication
- Use biometric authentication (Face ID/Touch ID)
- Review active sessions regularly
- Keep your Apple device updated
- Use strong, unique passwords
- Enable login notifications

❌ **DON'T:**
- Share your password with others
- Stay logged in on public or shared devices
- Ignore unfamiliar login notifications
- Disable security features for convenience
- Use the same password across multiple services

## Need Help?

- 📧 Email: Contact the repository owner through GitHub
- 📚 Documentation: [SECURITY.md](SECURITY.md)
- 🐛 Report Issues: Open an issue in this repository
- ❓ FAQ: Check the project wiki

---

**Last Updated**: December 2025 (Template)  
**Applies To**: All Apple devices (iPhone, iPad, Mac) running iOS 15+, iPadOS 15+, or macOS Monterey+
