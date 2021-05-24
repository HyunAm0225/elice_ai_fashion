import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'; 
import LandingPage from './pages/LandingPage';
import MainPage from './pages/MainPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import RegisterClosetPage from './pages/RegisterClosetPage';
import MyPage from './pages/MyPage';
import ImageUploadPage from './pages/ImageUploadPage';
import SimilarItemPage from './pages/SimilarItemPage';
import RecentItemPage from './pages/RecentItemPage';


function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={LandingPage} />
        <Route exact path="/main" component={MainPage} />
        <Route exact path="/login" component={LoginPage} />
        <Route exact path="/register" component={RegisterPage} />
        <Route exact path="/register/closet" component={RegisterClosetPage} />
        <Route exact path="/mypage" component={MyPage} />
        <Route exact path="/imgupload/:userid" component={ImageUploadPage} />
        <Route exact path="/smlritem/:userid" component={SimilarItemPage} />
        <Route exact path="/rcntitem/:userid" component={RecentItemPage} />
      </Switch>
    </Router>
  );
}

export default App;