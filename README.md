# CSGO-GSI (Game State Integration) - WIP

## Introduction
 
This project is meant to be an easy way to connect CS:GO (Counter Strike: Global Offensive) with an Arduino using the official GSI (Game State Integration) from Valve.

The doc for the GSI can be found here: https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration

As this is a widely used and documented solution, a player does not risk being banned from the server, which can happen if developing a third-party solution (such as screen recording / processing), which can lead to VAC bans.

## How does it work?

Basically, the game sends the information from the current match to an endpoint (via HTTP Post), which this application listens to.

The server is hosted locally, so there are no Buffer problems with too many connections/updates from the game.

This project is also responsible for sending the information from Python to a Serial COM Port, which will have an Arduino Board listening to in order to execute custom tasks.

## Functionalities

### Arduino

The Arduino board will be responsible for LEDs control for ingame events, such as:

- Player Death - Red Light
- Player Kill - Green Light
- Bomb Planted:
    - CT: Pulsating Red Light (on the same rhythm as the bomb ticking ingame)
    - T: Pulsating Blue Light (on the same rhythm as the bomb ticking ingame)
- Bomb Defused
    - CT: Green Light of victory
    - T: Red Light of defeat
- Player Flashed - Super bright LED (if I don't go almost blind in real life, it's not worth it xD)
- Player Smoked - Not entirely sure what color will I configure here, or the complete lack of light =/
- Player on fire - Orange / Red Pulsating Light

The board will also be responsible for some other stuff like:

- Vibrating the Chair/Table with a Vibration motor when taking damage / dying (easy and cheap)
- Smoke effect? Seems a bit over.. but why not? (kinda easy, but expensive)
- Fire effect (actual fire) - This one will be tricky, but same as the one above... why not? (dangerous, but actually pretty cheap :))

### Front-end Application

This application will be hosted on another Github repository (future link here, please be patient)