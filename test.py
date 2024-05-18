#!/usr/bin/python3
import cmd

class VoiceAssistant(cmd.Cmd):
    def onecmd(self, str):
        return super().onecmd(str)

    def do_lights_on(self, arg):
        print("Turning on the lights.")

assistant = VoiceAssistant()
assistant.onecmd('lights_on')

