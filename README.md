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


### Requirements

- Python 3.10+
- `cryptography` library
- `PyQt6`, `PyGObject`, or other UI libraries depending on the frontend you choose.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Equat-ion/permutations.git
   cd ./permutations/core
   ```

2. Run the application:

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

### Contributing

Contributions are welcomed! Feel free to submit a pull request or Contact me.


---

Enjoy managing your passwords with **Permutations**!

