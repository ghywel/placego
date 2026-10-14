<?php
/*
 * The store's private settings. Copy this file to ~/sharedstore-private/config.php (outside the web root) and fill
 * in the paths. The 'workers' lines come from make_token.php: it prints a token once (give it to that worker through
 * its own secret settings) and the line to paste here, which holds only the token's SHA-256, never the token itself.
 */
return [
    'data_dir'      => '/home/YOUR-ACCOUNT/sharedstore-private/data',
    'log_file'      => '/home/YOUR-ACCOUNT/sharedstore-private/store.log',
    'require_https' => true,
    'max_bytes'     => 64 * 1024 * 1024,
    // The whole store's cap. It shares the account's disk with the website, and cited/ files cannot be deleted through it.
    'max_total_bytes' => 2 * 1024 * 1024 * 1024,
    // Believe X-Forwarded-Proto only if the host sits behind a proxy that sets it (most cPanel hosts do not).
    'trust_forwarded_proto' => false,
    'workers'       => [
        // 'cloud' => 'sha256 of cloud's token',
        // 'local' => '...',
        // 'intel' => '...',
        // 'gpt'   => '...',
    ],
];
