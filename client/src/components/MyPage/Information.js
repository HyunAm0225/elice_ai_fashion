import { Box } from "@material-ui/core";
import useStyles from "styles/MyPageStyle";

function Information() {
  const classes = useStyles();

  return (
    <Box item className={classes.mobileInformationBox}>
      <Box className="mobileBoldText">정보</Box>
      <Box className={classes.mobileInfomationText}>앱 문의 건의</Box>
      <Box className={classes.mobileInfomationText}>공지사항</Box>
      <Box className={classes.mobileInfomationText}>버전 정보 0.0.1</Box>
    </Box>
  );
}

export default Information;
