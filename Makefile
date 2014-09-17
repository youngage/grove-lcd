HOST = ffpb-flasher
USER = pi
SRC  = backlight.py \
		 display.py \
		 screen.py

upload: $(SRC)
	pax -w $(SRC) | ssh $(USER)@$(HOST) "cd grove-lcd; tar xv"
