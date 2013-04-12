<!DOCTYPE html>
<html>
  <head>
    <title>Admin</title>
  </head>
  <body>
    <ul>
      %for page in pages:
        <li><a href="{{ get_url('admin_page', page=page.get('_id')) }}">{{ page.get('url') }}</a></li>
      %end
    </ul>
  </body>
</html>