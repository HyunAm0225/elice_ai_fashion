import React from "react";
import { Grid } from "@material-ui/core";
import useStyles from "../styles/MainPageStyle";
import { Mobile } from "../MediaQuery";

import Navbar from "../components/common/Navbar";
import Infinite from "../components/MainPage/Infinite";
import Category from "../components/MainPage/Category";
import ItemMain from "../components/MainPage/ItemMain";

function MainPage() {
  const classes = useStyles();

  return (
    <Mobile>
      <Navbar />
      <ItemMain />
      <Category />
      <Grid className={classes.mobileRoot}>
        <Grid container>
          <Infinite />
        </Grid>
      </Grid>
    </Mobile>
  );
}

export default MainPage;
