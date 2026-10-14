<?php
/*
 * make_token.php: run from a terminal (cPanel's Terminal or SSH), never from the web.
 *   php make_token.php cloud
 * prints a fresh random token for that worker, once, and the line to paste into config.php's 'workers'.
 * The token is not stored anywhere by this script. To revoke a worker, delete its line from config.php.
 */
if (PHP_SAPI !== 'cli') {
    http_response_code(404);
    exit;
}
$name = $argv[1] ?? '';
if (!preg_match('/^[a-z0-9-]{1,32}$/', $name)) {
    fwrite(STDERR, "usage: php make_token.php <worker-name, e.g. cloud>\n");
    exit(1);
}
$token = bin2hex(random_bytes(32));
echo "Token for '$name' (shown once; give it to that worker through its own secret settings, not by chat):\n";
echo "$token\n\n";
echo "Line for config.php, inside 'workers':\n";
echo "    '$name' => '" . hash('sha256', $token) . "',\n";
