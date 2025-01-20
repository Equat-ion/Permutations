# Permutations

**Permutations** is a local password manager built in Python. It allows users to securely store, view, update, and delete their passwords for various services. The app is modular and provides support for multiple user interfaces, including:

- **Qt6** (for KDE Plasma builds)
- **GTK4 Libadwaita** (for GNOME builds)
- **WinUI Mica** (for Windows builds)
- **TUI** (Text User Interface)

### Features

- **Secure Encryption**: Passwords are encrypted using the Fernet symmetric encryption algorithm from the `cryptography` library.
- **JSON-based Storage**: Passwords are stored in a lightweight, portable JSON file, eliminating the need for a database.
- **Cross-platform Compatibility**: The app supports Windows, macOS, and Linux, storing data in appropriate system-specific directories.
- **Modular Frontends**: Choose your preferred user interface, whether graphical or text-based.

### Directory Structure

```
permutations/
├── core/
│   ├── __init__.py
│   ├── core_app.py  # Main application logic
│   ├── database.py  # Handles JSON-based storage
│   └── encryption.py  # Handles encryption and decryption
├── frontends/
│   ├── qt6/  # Qt6 GUI for KDE
│   ├── gtk4/  # GTK4 Libadwaita GUI for GNOME
│   ├── winui/  # WinUI Mica interface for Windows
│   └── tui/  # Text-based user interface
├── README.md  # Project documentation
└── requirements.txt  # Python dependencies
```

### Requirements

- Python 3.10+
- `cryptography` library
- `PyQt6`, `PyGObject`, or other UI libraries depending on the frontend you choose.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/permutations.git
   cd permutations
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python -m core.core_app
   ```

### Usage

1. **Add a Password**: Input the service name, username, and password. The password is encrypted and saved.
2. **View Passwords**: Retrieve saved passwords. Decrypt them securely.
3. **Update Password**: Update an existing password for a service.
4. **Delete Password**: Remove a password entry from the database.

### Planned Features

- **UI Enhancements**: Full support for modular frontends.
- **Windows Installer**: Easy-to-use installer for Windows users.
- **Icon Design**: Custom app icon for better branding.

### Security Considerations

- Ensure the encryption key is securely stored and not exposed.
- Use the application in a trusted environment to prevent unauthorized access.

### Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

### License

This project is licensed under the GNU GPL v3 License.

---

Enjoy managing your passwords with **Permutations**!

