%rebase admin_layout.tpl get_url=get_url
<h2>{{ page.get('url') }}</h2>
<p><a href="{{ get_url('admin_page_delete', page=page.get('_id')) }}">Delete</a></p>
<form method="post" action="{{ get_url('admin_page', page=page.get('_id')) }}">
%include admin_page_form.tpl page=page
</form>
