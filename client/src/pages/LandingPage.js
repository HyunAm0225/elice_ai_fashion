import React, { useState } from 'react';
import { withStyles } from "@material-ui/core/styles";
import { Grid, Box, Button, Checkbox } from "@material-ui/core";
import { green } from '@material-ui/core/colors';
import useStyles from '../styles/LandingPageStyle';
import { Mobile } from "../MediaQuery";

const GreenCheckbox = withStyles({
  root: {
    color: green[400],
    '&$checked': {
      color: green[600],
    },
  },
  checked: {},
})((props) => <Checkbox color="default" {...props} />);

function LandingPage() {
  const classes = useStyles();
  const [select, setSelect] = useState(0);
  const [state, setState] = useState({});
  const checkList = [
    'checkedA', 'checkedB', 'checkedC', 'checkedD', 'checkedE',
    'checkedF', 'checkedG', 'checkedH', 'checkedI'
  ]

  const handleChange = (event) => {
    setState({ ...state, [event.target.name]: event.target.checked });
    event.target.checked ? setSelect(select+1): setSelect(select-1);
  };

  const images = checkList.map((check, idx) => (
    <Grid key={idx} item xs={4}>
      <Button className={state[check] ? classes.mobileImageActiveButton : classes.mobileImageButton}>
        <label className={classes.mobileImageLabel} htmlFor={check}></label>
        <img className={classes.mobileImage} src="images/clothes.png" alt="옷"></img>
        <Box className={classes.mobileCheckboxContainer}>
          <GreenCheckbox checked={state.check} onChange={handleChange} name={check} id={check} />
        </Box>
      </Button>
    </Grid>
  ))

  return (
    <Mobile>
    <Grid className={classes.mobileRoot}>
      <Grid className={classes.mobileNavbar}>
        {select >= 3 ? 
        <a href="/main" className={classes.mobileNavbarSelect}>선택하기</a> :
        <a href="/main" className={classes.mobileNavbarSkip}>건너뛰기</a> }
      </Grid>
      <Grid className={classes.mobileInfoMessageBox}>
        <Box className={classes.mobileInfoMessage}>스타일을 3개 이상 고르면<br />취향에 맞는 옷들을 추천해드릴게요 !</Box>
        <Box className={classes.mobileInfoMiniMessage}>많이 고르실수록 추천이 더욱더 정확해져요</Box>
      </Grid>
      <Grid container spacing={2} className={classes.mobileImageContainer}>
        {images}
      </Grid>
    </Grid>
    </Mobile>
  );
}

export default LandingPage;
