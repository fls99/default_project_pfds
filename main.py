from website import create_app

app = create_app()

# only run webserver when I run the file 
if __name__ == '__main__':
    app.run(debug=True)