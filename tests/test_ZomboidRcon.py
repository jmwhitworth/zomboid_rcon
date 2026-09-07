import unittest
from unittest.mock import MagicMock

from zomboid_rcon import CommandResult, ZomboidRcon


def make_success_result(command="test"):
    return CommandResult(command, "OK", successful=True)


class ZomboidRcon_test(unittest.TestCase):
    def setUp(self):
        self.pz = ZomboidRcon()
        self.pz.command = MagicMock(return_value=make_success_result())

    def test_constructor_defaults(self):
        pz = ZomboidRcon()
        self.assertEqual(pz._ip, "localhost")
        self.assertEqual(pz._port, 27015)
        self.assertEqual(pz._password, "pzserver")
        self.assertEqual(pz._retries, 5)
        self.assertFalse(pz.logging)

    def test_constructor_accepts_custom_values(self):
        pz = ZomboidRcon(ip="10.0.0.1", port=1234, password="pass", retries=3, logging=True)
        self.assertEqual(pz._ip, "10.0.0.1")
        self.assertEqual(pz._port, 1234)
        self.assertEqual(pz._password, "pass")
        self.assertEqual(pz._retries, 3)
        self.assertTrue(pz.logging)

    # --- General commands ---

    def test_players(self):
        self.pz.players()
        self.pz.command.assert_called_once_with("players")

    def test_save(self):
        self.pz.save()
        self.pz.command.assert_called_once_with("save")

    def test_quit(self):
        self.pz.quit()
        self.pz.command.assert_called_once_with("quit")

    def test_additem_without_count(self):
        self.pz.additem("user1", "Base.Axe")
        self.pz.command.assert_called_once_with("additem", "user1", "Base.Axe")

    def test_additem_with_count(self):
        self.pz.additem("user1", "Base.Axe", 5)
        self.pz.command.assert_called_once_with("additem", "user1", "Base.Axe", "5")

    def test_addkey_without_name(self):
        self.pz.addkey("user1", 7295)
        self.pz.command.assert_called_once_with("addkey", "user1", "7295")

    def test_addkey_with_name(self):
        self.pz.addkey("user1", 7295, "Gift Key")
        self.pz.command.assert_called_once_with(
            "addkey", "user1", "7295", "Gift Key"
        )

    def test_addsteamid(self):
        self.pz.addsteamid("76561198000000000")
        self.pz.command.assert_called_once_with(
            "addSteamID", "76561198000000000"
        )

    def test_addtosafehouse_passes_undocumented_arguments(self):
        self.pz.addtosafehouse("user1", "safehouse")
        self.pz.command.assert_called_once_with(
            "addtosafehouse", "user1", "safehouse"
        )

    def test_addvehicle(self):
        self.pz.addvehicle("Base.VanSeats", "user1")
        self.pz.command.assert_called_once_with("addvehicle", "Base.VanSeats", "user1")

    def test_addxp_formats_perk_correctly(self):
        self.pz.addxp("user1", "Strength", 100)
        self.pz.command.assert_called_once_with("addxp", "user1", "Strength=100")

    def test_clear(self):
        with self.assertWarns(UserWarning):
            self.pz.clear()
        self.pz.command.assert_called_once_with("clear")

    def test_createhorde2_passes_undocumented_arguments(self):
        self.pz.createhorde2("10", "user1")
        self.pz.command.assert_called_once_with("createhorde2", "10", "user1")

    def test_createhorde_without_user(self):
        self.pz.createhorde(50)
        self.pz.command.assert_called_once_with("createhorde", "50")

    def test_createhorde_with_user(self):
        self.pz.createhorde(50, "user1")
        self.pz.command.assert_called_once_with("createhorde", "50", "user1")

    def test_godmode_default_true(self):
        self.pz.godmode("user1")
        self.pz.command.assert_called_once_with("godmode", "user1", "-true")

    def test_godmode_false(self):
        self.pz.godmode("user1", False)
        self.pz.command.assert_called_once_with("godmode", "user1", "-false")

    def test_invisible_default_true(self):
        self.pz.invisible("user1")
        self.pz.command.assert_called_once_with("invisible", "user1", "-true")

    def test_invisible_false(self):
        self.pz.invisible("user1", False)
        self.pz.command.assert_called_once_with("invisible", "user1", "-false")

    def test_godmodeplayer(self):
        self.pz.godmodeplayer("user1", False)
        self.pz.command.assert_called_once_with(
            "godmodeplayer", "user1", "-false"
        )

    def test_help_for_command(self):
        self.pz.help("worldgen")
        self.pz.command.assert_called_once_with("help", "worldgen")

    def test_invisibleplayer(self):
        self.pz.invisibleplayer("user1")
        self.pz.command.assert_called_once_with(
            "invisibleplayer", "user1", "-true"
        )

    def test_lightning_without_user(self):
        self.pz.lightning()
        self.pz.command.assert_called_once_with("lightning")

    def test_lightning_with_user(self):
        self.pz.lightning("user1")
        self.pz.command.assert_called_once_with("lightning", "user1")

    def test_log(self):
        self.pz.log("General", "Debug")
        self.pz.command.assert_called_once_with("log", "General", "Debug")

    def test_noclip_default_true(self):
        self.pz.noclip("user1")
        self.pz.command.assert_called_once_with("noclip", "user1", "-true")

    def test_noclip_false(self):
        self.pz.noclip("user1", False)
        self.pz.command.assert_called_once_with("noclip", "user1", "-false")

    def test_startrain_without_intensity(self):
        self.pz.startrain()
        self.pz.command.assert_called_once_with("startrain")

    def test_startrain_with_intensity(self):
        self.pz.startrain(75)
        self.pz.command.assert_called_once_with("startrain", "75")

    def test_startstorm_without_duration(self):
        self.pz.startstorm()
        self.pz.command.assert_called_once_with("startstorm")

    def test_startstorm_with_duration(self):
        self.pz.startstorm(6)
        self.pz.command.assert_called_once_with("startstorm", "6")

    def test_stats_without_period(self):
        self.pz.stats("file")
        self.pz.command.assert_called_once_with("stats", "file")

    def test_stats_with_period(self):
        self.pz.stats("file", 10)
        self.pz.command.assert_called_once_with("stats", "file", "10")

    def test_stopweather(self):
        self.pz.stopweather()
        self.pz.command.assert_called_once_with("stopweather")

    def test_teleport_single_arg(self):
        self.pz.teleport("user1")
        self.pz.command.assert_called_once_with("teleport", "user1")

    def test_teleport_two_args(self):
        self.pz.teleport("user1", "user2")
        self.pz.command.assert_called_once_with("teleport", "user1", "user2")

    def test_teleportplayer(self):
        self.pz.teleportplayer("user1", "user2")
        self.pz.command.assert_called_once_with(
            "teleportplayer", "user1", "user2"
        )

    def test_teleportto_formats_coordinates(self):
        self.pz.teleportto(100, 200, 0)
        self.pz.command.assert_called_once_with("teleportto", "100,200,0")

    def test_thunder_without_user(self):
        self.pz.thunder()
        self.pz.command.assert_called_once_with("thunder")

    def test_thunder_with_user(self):
        self.pz.thunder("user1")
        self.pz.command.assert_called_once_with("thunder", "user1")

    def test_servermsg_replaces_spaces_with_underscores(self):
        self.pz.servermsg("Hello world")
        self.pz.command.assert_called_once_with("servermsg", "Hello_world")

    def test_servermsg_strips_leading_trailing_whitespace(self):
        self.pz.servermsg("  Hello  ")
        self.pz.command.assert_called_once_with("servermsg", "Hello")

    def test_replay_warns_that_build_42_removed_it(self):
        with self.assertWarns(UserWarning):
            self.pz.replay("user1", "-record", "test.bin")
        self.pz.command.assert_called_once_with(
            "replay", "user1", "-record", "test.bin"
        )

    # --- Moderation commands ---

    def test_banuser_user_only(self):
        self.pz.banuser("badguy")
        self.pz.command.assert_called_once_with("banuser", "badguy")

    def test_banuser_with_ip(self):
        self.pz.banuser("badguy", ip=True)
        self.pz.command.assert_called_once_with("banuser", "badguy", "-ip")

    def test_banuser_with_reason(self):
        self.pz.banuser("badguy", reason="spawn kill")
        self.pz.command.assert_called_once_with("banuser", "badguy", "-r", "spawn kill")

    def test_banuser_with_ip_and_reason(self):
        self.pz.banuser("badguy", ip=True, reason="spawn kill")
        self.pz.command.assert_called_once_with("banuser", "badguy", "-ip", "-r", "spawn kill")

    def test_unbanuser(self):
        self.pz.unbanuser("badguy")
        self.pz.command.assert_called_once_with("unbanuser", "badguy")

    def test_banip(self):
        self.pz.banip("192.0.2.1")
        self.pz.command.assert_called_once_with("banip", "192.0.2.1")

    def test_unbanip(self):
        self.pz.unbanip("192.0.2.1")
        self.pz.command.assert_called_once_with("unbanip", "192.0.2.1")

    def test_kickuser(self):
        self.pz.kickuser("someuser")
        self.pz.command.assert_called_once_with("kickuser", "someuser")

    def test_kickuser_with_reason(self):
        self.pz.kickuser("someuser", reason="spawn kill")
        self.pz.command.assert_called_once_with(
            "kickuser", "someuser", "-r", "spawn kill"
        )

    def test_kickfromsafehouse_passes_undocumented_arguments(self):
        self.pz.kickfromsafehouse("someuser")
        self.pz.command.assert_called_once_with("kickfromsafehouse", "someuser")

    def test_list_passes_undocumented_arguments(self):
        self.pz.list("players")
        self.pz.command.assert_called_once_with("list", "players")

    def test_grantadmin(self):
        self.pz.grantadmin("someuser")
        self.pz.command.assert_called_once_with("grantadmin", "someuser")

    def test_removeadmin(self):
        self.pz.removeadmin("someuser")
        self.pz.command.assert_called_once_with("removeadmin", "someuser")

    def test_setaccesslevel(self):
        self.pz.setaccesslevel("someuser", "moderator")
        self.pz.command.assert_called_once_with("setaccesslevel", "someuser", "moderator")

    def test_adduser(self):
        self.pz.adduser("newuser", "password123")
        self.pz.command.assert_called_once_with("adduser", "newuser", "password123")

    def test_reloadalllua(self):
        self.pz.reloadalllua()
        self.pz.command.assert_called_once_with("reloadalllua")

    def test_remove_passes_undocumented_arguments(self):
        self.pz.remove("object")
        self.pz.command.assert_called_once_with("remove", "object")

    def test_removeitem(self):
        self.pz.removeitem("Base.Axe", 5)
        self.pz.command.assert_called_once_with("removeitem", "Base.Axe", "5")

    def test_removemapsymbolsforuser(self):
        self.pz.removemapsymbolsforuser("user1")
        self.pz.command.assert_called_once_with(
            "removemapsymbolsforuser", "user1"
        )

    def test_removesteamid(self):
        self.pz.removesteamid("76561198000000000")
        self.pz.command.assert_called_once_with(
            "removeSteamID", "76561198000000000"
        )

    def test_removezombies_passes_undocumented_arguments(self):
        self.pz.removezombies("user1")
        self.pz.command.assert_called_once_with("removezombies", "user1")

    def test_setpassword(self):
        self.pz.setpassword("user1", "newpassword")
        self.pz.command.assert_called_once_with(
            "setpassword", "user1", "newpassword"
        )

    def test_worldgen(self):
        self.pz.worldgen("status")
        self.pz.command.assert_called_once_with("worldgen", "status")
