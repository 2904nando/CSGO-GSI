# CSGO-GSI (Game State Integration) - WIP

## Introduction
 
This project is meant to be an easy way to connect CS:GO (Counter Strike: Global Offensive) with an Arduino using the official GSI (Game State Integration) from Valve.

The doc for the GSI can be found here: https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration

As this is a widely used and documented solution, a player does not risk being banned from the server, which can happen if developing a third-party solution (such as screen recording / processing), which can lead to VAC bans.

## How does it work?

Basically, the game sends the information from the current match to an endpoint (via HTTP Post), which this application listens to.

The server is hosted locally, so there are no Buffer problems with too many connections/updates from the game.

This project is also responsible for sending the information from Python to a Serial COM Port, which will have an Arduino Board listening to in order to execute custom tasks.