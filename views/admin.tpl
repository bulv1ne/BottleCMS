%rebase admin_layout.tpl get_url=get_url
<ul>
  %for page in pages:
    <li><a href="{{ get_url('admin_page', page=page.get('_id')) }}">{{ page.get('url') }}</a></li>
  %end
</ul>
