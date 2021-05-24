import { Box } from "@material-ui/core";
import useStyles from "../../styles/MyPageStyle";

function Information() {
  const classes = useStyles();

  return (
    <Box item className={classes.mobileInformationBox}>
      <Box className={classes.mobileBoldText}>정보</Box>
      <Box>앱 문의 건의</Box>
      <Box>공지사항</Box>
      <Box>버전 정보 0.0.0</Box>
    </Box>
  );
}

export default Information;
