<dl>
  <dt>URL</dt>
  <dd><input name="url" value="{{ page.get('url','') }}" /></dd>
  <dt>Template</dt>
  <dd><input name="template" value="{{ page.get('template','') }}" /></dd>
  <dt>Title</dt>
  <dd><input name="title" value="{{ page.get('title','') }}" /></dd>
  <dt>Content</dt>
  <dd><textarea name="content">{{ page.get('content','') }}</textarea></dd>
</dl>
<input type="submit" value="Save" />