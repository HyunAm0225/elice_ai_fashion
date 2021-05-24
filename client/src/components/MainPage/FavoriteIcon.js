import React, { useState } from "react";
import StarsIcon from "@material-ui/icons/Stars";
import { Checkbox, Box } from "@material-ui/core";
import "../../App.css";

export default function FavoriteIcon({ idx }) {
  const [favorite, setFavorite] = useState({});

  const handleChange = (event) => {
    setFavorite({ ...favorite, [event.target.name]: event.target.checked });
  };

  return (
    <Box>
      <Checkbox
        style={{ padding: "0" }}
        checked={favorite.idx}
        onChange={handleChange}
        icon={<StarsIcon style={{ color: "var(--color-bg-dark)" }} />}
        checkedIcon={<StarsIcon style={{ color: "var(--color-main-a)" }} />}
        name={idx}
      />
    </Box>
  );
}
