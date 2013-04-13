%rebase admin_layout.tpl get_url=get_url
<h2>{{ page.get('url') }}</h2>
<form method="post" action="{{ get_url('admin_page', page=page.get('_id')) }}">
  <dl>
    <dt>URL</dt>
    <dd><input name="url" value="{{ page.get('url') }}" /></dd>
    <dt>Template</dt>
    <dd><input name="template" value="{{ page.get('template') }}" /></dd>
    <dt>Title</dt>
    <dd><input name="title" value="{{ page.get('title') }}" /></dd>
    <dt>Content</dt>
    <dd><textarea name="content">{{ page.get('content') }}</textarea></dd>
  </dl>
  <input type="submit" />
</form>
