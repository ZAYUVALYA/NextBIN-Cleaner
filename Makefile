PACKAGE = nextbin
VERSION = 1.0
BUILD_DIR = build

all:
	dpkg-deb --build $(PACKAGE) $(BUILD_DIR)/$(PACKAGE)-$(VERSION).deb
