import sublime, sublime_plugin
import desktop
import tempfile
import markdown
import os
import yaml, re
import urllib
import urllib2

class TumblrManager():
    def __init__(self):
        self.settings = {}
        settings = sublime.load_settings(__name__ + '.sublime-settings')
        self.settings['email'] = settings.get('email')
        self.settings['password'] = settings.get('password')

    def load_front_matter(self, content):
        sub_content = re.search( r'(\s*---\s*.*\s*---)', content, re.MULTILINE|re.DOTALL)
        # print sub_content.group()
        front_matters = yaml.load_all(sub_content.group())
        front_matter = list(front_matters)
        front_matter = front_matter[0]
        request_data = {}
        request_data['email'] = self.settings['email']
        request_data['password'] = self.settings['password']
        if front_matter.has_key('title'):
            request_data['title'] = front_matter['title']
        if front_matter.has_key('categories'):
            request_data['tags'] = front_matter['categories']
        if front_matter.has_key('date'):
            request_data['date'] = front_matter['date']
        print request_data
        return request_data

    def post_to_tumblr(self, content, draft):
        request_data = self.load_front_matter(content)
        sub_content = re.sub( re.compile(r'(\s*---\s*.*\s*---)',  re.MULTILINE|re.DOTALL), "", content)
        print sub_content
        markdown_html = markdown.markdown(sub_content)
        request_data['body'] = markdown_html
        if draft:
            request_data['state'] = "draft"
        encoded_data = urllib.urlencode(request_data)
        req = urllib2.Request('http://www.tumblr.com/api/write')
        res = urllib2.urlopen(req, encoded_data).read()
        print res

class MarkdownPreviewCommand(sublime_plugin.TextCommand):
    """ preview file contents with python-markdown and your web browser"""

    def getCSS(self):
        css_filename = 'markdown.css'
        # path via package manager
        css_path = os.path.join(sublime.packages_path(), 'Markdown Preview', css_filename)
        if not os.path.isfile(css_path):
            # path via git repo
            css_path = os.path.join(sublime.packages_path(), 'sublimetext-markdown-preview', css_filename)
            if not os.path.isfile(css_path):
                raise Exception("markdown.css file not found!")

        return open(css_path, 'r').read()

    def run(self, edit, target='browser'):
        print edit, target
        region = sublime.Region(0, self.view.size())
        encoding = self.view.encoding()
        if encoding == 'Undefined':
            encoding = 'UTF-8'
        elif encoding == 'Western (Windows 1252)':
            encoding = 'windows-1252'
        view_contents = self.view.substr(region)

        # convert the markdown
        markdown_html = markdown.markdown(view_contents)

        # build the html
        html_contents = u'<meta charset="%s">' % self.view.encoding()
        styles = self.getCSS()
        html_contents += '<style>%s</style>' % styles
        html_contents += markdown_html
        # output
        if target == 'browser':
            tmp_html = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
            tmp_html.write(html_contents.encode(encoding))
            tmp_html.close()
            desktop.open(tmp_html.name)
        elif target == 'sublime':
            new_view = self.view.window().new_file()
            new_edit = new_view.begin_edit()
            new_view.insert(new_edit, 0, html_contents)
            new_view.end_edit(new_edit)
        elif target == 'tumblr':
            tumblr = TumblrManager()
            tumblr.post_to_tumblr(view_contents, False)
        elif target == 'tumblr_draft':
            tumblr = TumblrManager()
            tumblr.post_to_tumblr(view_contents, True)
