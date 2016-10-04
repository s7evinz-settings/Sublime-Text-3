import sublime, sublime_plugin

class BindRepeatMotion(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        for i in range(args['motion_args']['amount']):
            self.view.run_command('set_motion', args)
