local ccb = require("ccb")

ccb.runtime.handler("welcome", function()
    ccb.services.message("CCB Docs Platform v1 example is running.")
end)

ccb.runtime.on("world_ready", "welcome")
