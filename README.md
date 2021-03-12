# Create-react-app with flask backend test
The app is deployed with two heroku apps.

Frontend: [Heroku-link](https://heroku-cra-test.herokuapp.com/)  
Backend: [Heroku-link](https://heroku-cra-test-backend.herokuapp.com/time)  

## Frontend
### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

## Backend
create a virtual enviroment, open and and install all requirements with pip.

```
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

You can now run the backend server locally at [http://localhost:5000](http://localhost:5000) with
```
flask run
```