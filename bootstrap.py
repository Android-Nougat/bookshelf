from flask import Flask,url_for,redirect,request,render_template
app=Flask(__name__)
@app.route("/")
def home():
	cart=[{id:1,"name":"Notebooks","img":"https://images.unsplash.com/photo-1531346878377-a5be20888e57?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"},
	{id:1,"name":"Harry Potter and the Cursed Child","img":"https://vignette.wikia.nocookie.net/harrypotter/images/1/14/Harry_Potter_and_the_Cursed_Child_Script_Book_Cover.jpg/revision/latest/top-crop/width/360/height/450?cb=20160726165903"},
	{id:2,"name":"Harry Potter Collection","img":"https://akm-img-a-in.tosshub.com/indiatoday/images/story/201909/harry_potter_books_1.jpeg?QmKwhUZNh_VWGzMlbYBuDw3ElHnr67EB&size=770:433"},
	{id:3,"name":"Game of Thrones Collection","img":"https://rukminim1.flixcart.com/image/352/352/jpr86fk0/book/1/5/9/game-of-thrones-the-story-continues-7-book-boxset-original-imafbxc4f5xe3fha.jpeg?q=70"},
	{id:4,"name":"Seven Eves","img":"data:image/jpeg;base64,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"},
	{id:5,"name":"Permanant Record","img":"https://images-na.ssl-images-amazon.com/images/I/51YOZrqKhBL._SX323_BO1,204,203,200_.jpg"}]
	return render_template("child.html",cart=cart)
@app.route("/login",methods=["POST","GET"])
def login():
	if(request.method=="POST"):
		user=request.form["user"];
		return redirect(url_for("auth",user=user))
	else:
		return render_template("login.html",user="Dead")

@app.route("/<user>")
def auth(user):
	return render_template("child.html")
if __name__=="__main__":
	app.debug=True
	app.run()
	app.run(debug=True)