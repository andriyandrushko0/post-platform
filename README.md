<h1>Simple post platform based on Django Rest Framework</h1>
<p>By Andriy Andrushko</p>
<h4><a href="https://djd-post.herokuapp.com">Project on Heroku</a></h4>
<h6>Contents</h6>
<ul>
    <li><a href="#description">Description</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#api">Api usage</a></li>
</ul>
<br>
<div name="description">
    <h3>Description</h3>
    <p>Simple Django app for managin posts and comments. 
    CRUD for models are based on Django Rest Framework.<br>
    <h6>Implemented two models:</h6>Post and PostComment</p>
    <h4>Post model attributes</h4>
    <ul>
        <li><code>title</code> - title of the post</li>
        <li><code>link</code> - link to the post</li>
        <li><code>creation_date</code> - date and time creations</li>
        <li><code>amount_of_upvotes</code> - number of upvotes</li>
        <li><code>author_name</code> - author name</li>
    </ul>
    <h4>PostComment model attributes</h4>
    <ul>
        <li><code>post</code> - related field, refers to Post model</li>
        <li><code>conten</code> - content of the comment</li>
        <li><code>creation_date</code> - date and time creations</li>
        <li><code>author_name</code> - author name</li>
    </ul>
</div>
<br>
<div name="installation">
    <h3>Installation</h3>
    <ul>
        <li>Install Docker</li>
        <li>Clone repository</li>
    </ul>
</div>
<br>
<div name="usage">
    <h3>Usage</h3>
    <h5>Run project</h5>
    <ul>
        <li>Move to project folder</li>
        <li>Run command <code>docker-compose build</code> to build project</li>
        <li>Run command <code>docker-compose up</code> to run project</li>
        <li><b>Important! Run this command to migrate</b> <code>docker-compose exec web python manage.py migrate --noinput</code></li>
    </ul>
    <h5>Manage environment</h5>
    <ul>
        <li>Move to project folder</li>
        <li>Edit file <code> .env.dev </code></li>
    </ul>
</div>
<br>
<div name="api">
    <h3>Api usage</h3>
    <h5>Post model CRUD</h5>
    <ul>
        <li><code>GET</code> - <code>{{basic_url}}api/posts/</code><br>Returns list of posts</li>
        <li><code>GET</code> - <code>{{basic_url}}api/posts/{{id}}</code><br>Returns details of post with <code>id={{id}}</code></li>
        <li><code>POST</code> - <code>{{basic_url}}api/posts/</code><br>Creates new post with required arguments</code></li>
        <li><code>PUT</code> - <code>{{basic_url}}api/posts/{{id}}</code><br>Updates post with <code>id={{id}}</code></li>
        <li><code>DELETE</code> - <code>{{basic_url}}api/posts/{{id}}</code><br>Deletes post with <code>id={{id}}</code></li>
    </ul>
    <h5>PostComment model CRUD</h5>
    <ul>
        <li><code>GET</code> - <code>{{basic_url}}api/comments/</code><br>Returns list of comments</li>
        <li><code>GET</code> - <code>{{basic_url}}api/comments/{{id}}</code><br>Returns details of comment with <code>id={{id}}</code></li>
        <li><code>POST</code> - <code>{{basic_url}}api/comments/</code><br>Creates new comment with required arguments</code></li>
        <li><code>PUT</code> - <code>{{basic_url}}api/comments/{{id}}</code><br>Updates comment with <code>id={{id}}</code></li>
        <li><code>DELETE</code> - <code>{{basic_url}}api/comments/{{id}}</code><br>Deletes comment with <code>id={{id}}</code></li>
    </ul>
    <h3>For more detailed docs use this link <a href="https://documenter.getpostman.com/view/14636259/TWDWLxz3">Documentation at Postman</a></h3>
</div>
