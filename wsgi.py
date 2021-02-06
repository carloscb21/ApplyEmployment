from server import application

if __name__ == '__main__':
    import os
    application.run(debug=True, use_reloader=False, port=os.environ.get('PORT', 5000))
