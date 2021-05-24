import { Box, Button } from "@material-ui/core";
import { useHistory } from "react-router-dom";
import useStyles from "../../styles/MyPageStyle";

function Welcome() {
  const classes = useStyles();
  const history = useHistory();
  const title = "안녕하세요 (닉네임) !";

  return (
    <Box className={classes.mobileWelcomeBox}>
      <Box className={classes.mobileWelcomeText}>{title}</Box>
      <Button
        onClick={() => {
          history.push({ pathname: "/login" });
        }}
        className={classes.mobileCategoryButton}
      >
        로그아웃
      </Button>
    </Box>
  );
}

export default Welcome;
