import React, { Component } from 'react';
import Tabbar from '@TABBAR_PATH/tabbar';
import Ranking from '@HOME_PATH/ranking';
import About from '@MINE_PATH/about';
import store from './redux/store/Store';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route } from 'react-router-dom';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Router>
          <div>
            <Route path="/" component={Tabbar} />
            <Route path="/Ranking" component={Ranking} />
            <Route path="/About" component={About} />
          </div>
        </Router>
      </Provider>
    );
  }
}

export default App;
